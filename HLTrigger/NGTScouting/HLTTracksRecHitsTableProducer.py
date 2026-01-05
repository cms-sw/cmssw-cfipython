import FWCore.ParameterSet.Config as cms

def HLTTracksRecHitsTableProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTTracksRecHitsTableProducer',
    maxRecHits = cms.uint32(16),
    skipNonExistingSrc = cms.bool(False),
    tableName = cms.required.string,
    tracksSrc = cms.required.InputTag,
    precision = cms.int32(7),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
