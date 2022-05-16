import FWCore.ParameterSet.Config as cms

siPixelDigisSoAFromCUDA = cms.EDProducer('SiPixelDigisSoAFromCUDA',
  src = cms.InputTag('siPixelClustersCUDA'),
  mightGet = cms.optional.untracked.vstring
)
