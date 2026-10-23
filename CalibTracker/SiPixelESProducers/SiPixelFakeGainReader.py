import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeGainReader',
    fileName = cms.string('out.root'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
