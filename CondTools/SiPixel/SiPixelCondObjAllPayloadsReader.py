import FWCore.ParameterSet.Config as cms

def SiPixelCondObjAllPayloadsReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjAllPayloadsReader',
    payloadType = cms.string('HLT'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
