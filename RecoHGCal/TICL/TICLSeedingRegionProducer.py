import FWCore.ParameterSet.Config as cms

def TICLSeedingRegionProducer(*args, **kwargs):
  mod = cms.EDProducer('TICLSeedingRegionProducer',
    seedingPSet = cms.PSet(
      algo_verbosity = cms.int32(0),
      type = cms.string('SeedingRegionGlobal')
    
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
