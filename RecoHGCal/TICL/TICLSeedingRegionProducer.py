import FWCore.ParameterSet.Config as cms

def TICLSeedingRegionProducer(**kwargs):
  mod = cms.EDProducer('TICLSeedingRegionProducer',
    seedingPSet = cms.PSet(
      algo_verbosity = cms.int32(0),
      type = cms.string('SeedingRegionGlobal')
    
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
