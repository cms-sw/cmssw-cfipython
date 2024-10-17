import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainOfflineReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeGainOfflineReader',
    fileName = cms.string('out.root'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
