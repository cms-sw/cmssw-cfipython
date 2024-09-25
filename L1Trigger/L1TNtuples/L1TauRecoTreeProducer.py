import FWCore.ParameterSet.Config as cms

def L1TauRecoTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TauRecoTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
