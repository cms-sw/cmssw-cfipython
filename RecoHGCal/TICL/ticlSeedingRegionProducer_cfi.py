import FWCore.ParameterSet.Config as cms

ticlSeedingRegionProducer = cms.EDProducer('TICLSeedingRegionProducer',
  seedingPSet = cms.PSet(
    algo_verbosity = cms.int32(0),
    type = cms.string('SeedingRegionGlobal')
  
  ),
  mightGet = cms.optional.untracked.vstring
)
