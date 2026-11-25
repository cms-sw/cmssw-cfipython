import FWCore.ParameterSet.Config as cms

def MtdSimMergedClusterToTPAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdSimMergedClusterToTPAssociatorEDProducer',
    associator = cms.InputTag('mtdSimMergedClusterToTPAssociatorByTrackId'),
    mtdSimMergedClustersTag = cms.InputTag('mtdSimMergedClusterProducer'),
    trackingParticlesTag = cms.InputTag('mix', 'MergedTrackTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
