import FWCore.ParameterSet.Config as cms

def SimTracksterTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SimTracksterTableProducer',
    tableName = cms.string('hltSimTrackstersTable'),
    skipNonExistingSrc = cms.bool(False),
    simTracksters = cms.InputTag('hltTiclSimTracksters'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    simClusters = cms.InputTag('mix', 'MergedCaloTruth'),
    caloParticleToSimClustersMap = cms.InputTag('hltTiclSimTracksters'),
    precision = cms.int32(7),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
