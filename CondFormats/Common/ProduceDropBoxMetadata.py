import FWCore.ParameterSet.Config as cms

def ProduceDropBoxMetadata(**kwargs):
  mod = cms.EDAnalyzer('ProduceDropBoxMetadata',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
