import FWCore.ParameterSet.Config as cms

def PCLMetadataWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('PCLMetadataWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
