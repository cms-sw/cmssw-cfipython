import FWCore.ParameterSet.Config as cms

siPixelDigiErrorsSoAFromCUDA = cms.EDProducer('SiPixelDigiErrorsSoAFromCUDA',
  src = cms.InputTag('siPixelClustersCUDA'),
  mightGet = cms.optional.untracked.vstring
)
