import FWCore.ParameterSet.Config as cms

siPixelDigisClustersFromSoA = cms.EDProducer('SiPixelDigisClustersFromSoA',
  src = cms.InputTag('siPixelDigisSoA'),
  mightGet = cms.optional.untracked.vstring
)
