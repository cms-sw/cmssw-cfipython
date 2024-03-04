import FWCore.ParameterSet.Config as cms

def HLTL1TMuonSelector(**kwargs):
  mod = cms.EDProducer('HLTL1TMuonSelector',
    InputObjects = cms.InputTag('hltGmtStage2Digis'),
    L1MinPt = cms.double(-1),
    L1MaxEta = cms.double(5),
    L1MinQuality = cms.uint32(0),
    CentralBxOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
