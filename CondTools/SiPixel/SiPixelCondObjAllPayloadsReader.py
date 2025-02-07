import FWCore.ParameterSet.Config as cms

def SiPixelCondObjAllPayloadsReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjAllPayloadsReader',
    payloadType = cms.string('HLT'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
