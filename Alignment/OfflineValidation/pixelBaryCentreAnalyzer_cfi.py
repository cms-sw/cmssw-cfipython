import FWCore.ParameterSet.Config as cms

pixelBaryCentreAnalyzer = cms.EDAnalyzer('PixelBaryCentreAnalyzer',
  usePixelQuality = cms.untracked.bool(False),
  tkAlignLabels = cms.untracked.vstring(),
  beamSpotLabels = cms.untracked.vstring(),
  mightGet = cms.optional.untracked.vstring
)
