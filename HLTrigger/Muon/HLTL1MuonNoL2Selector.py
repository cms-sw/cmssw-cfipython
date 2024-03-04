import FWCore.ParameterSet.Config as cms

def HLTL1MuonNoL2Selector(**kwargs):
  mod = cms.EDProducer('HLTL1MuonNoL2Selector',
    InputObjects = cms.InputTag(''),
    L2CandTag = cms.InputTag('hltL2MuonCandidates'),
    SeedMapTag = cms.InputTag('hltL2Muons'),
    L1MinPt = cms.double(-1),
    L1MaxEta = cms.double(5),
    L1MinQuality = cms.uint32(0),
    CentralBxOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
