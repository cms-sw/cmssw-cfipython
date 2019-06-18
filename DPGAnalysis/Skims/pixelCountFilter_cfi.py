import FWCore.ParameterSet.Config as cms

pixelCountFilter = cms.EDFilter('PixelCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
