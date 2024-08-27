import FWCore.ParameterSet.Config as cms

def PixelBaryCentreAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PixelBaryCentreAnalyzer',
    usePixelQuality = cms.untracked.bool(False),
    tkAlignLabels = cms.untracked.vstring(),
    beamSpotLabels = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
