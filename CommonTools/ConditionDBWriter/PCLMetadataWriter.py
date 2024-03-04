import FWCore.ParameterSet.Config as cms

def PCLMetadataWriter(**kwargs):
  mod = cms.EDAnalyzer('PCLMetadataWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
