import FWCore.ParameterSet.Config as cms

def ProduceDropBoxMetadata(*args, **kwargs):
  mod = cms.EDAnalyzer('ProduceDropBoxMetadata',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
