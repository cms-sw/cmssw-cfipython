import FWCore.ParameterSet.Config as cms

def HLTL1MuonSelector(*args, **kwargs):
  mod = cms.EDProducer('HLTL1MuonSelector',
    InputObjects = cms.InputTag(''),
    L1MinPt = cms.double(-1),
    L1MaxEta = cms.double(5),
    L1MinQuality = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
