import FWCore.ParameterSet.Config as cms

def MuonColMerger(*args, **kwargs):
  mod = cms.EDProducer('MuonColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
