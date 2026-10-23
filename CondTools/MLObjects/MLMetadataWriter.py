import FWCore.ParameterSet.Config as cms

def MLMetadataWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('MLMetadataWriter',
    model = cms.PSet(
      model_name = cms.required.string,
      version = cms.required.int32,
      hash = cms.required.string
    ),
    since = cms.required.uint64,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
