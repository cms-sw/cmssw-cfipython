import FWCore.ParameterSet.Config as cms

ticlSeedingRegionProducer = cms.EDProducer('TICLSeedingRegionProducer',
  algo_verbosity = cms.int32(0),
  tracks = cms.InputTag('generalTracks'),
  cutTk = cms.string('1.48 < abs(eta) < 3.0 && pt > 2. && quality("highPurity") && hitPattern().numberOfLostHits("MISSING_OUTER_HITS") < 10'),
  propagator = cms.string('PropagatorWithMaterial'),
  algoId = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
