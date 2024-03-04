import FWCore.ParameterSet.Config as cms

def HLTL1MuonSelector(**kwargs):
  mod = cms.EDProducer('HLTL1MuonSelector',
    InputObjects = cms.InputTag(''),
    L1MinPt = cms.double(-1),
    L1MaxEta = cms.double(5),
    L1MinQuality = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
