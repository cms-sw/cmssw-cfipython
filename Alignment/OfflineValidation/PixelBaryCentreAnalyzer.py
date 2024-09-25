import FWCore.ParameterSet.Config as cms

def PixelBaryCentreAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelBaryCentreAnalyzer',
    usePixelQuality = cms.untracked.bool(False),
    tkAlignLabels = cms.untracked.vstring(),
    beamSpotLabels = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
