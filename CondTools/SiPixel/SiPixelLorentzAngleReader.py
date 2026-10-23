import FWCore.ParameterSet.Config as cms

def SiPixelLorentzAngleReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelLorentzAngleReader',
    recoLabel = cms.string(''),
    simLabel = cms.string(''),
    printDebug = cms.untracked.uint32(10),
    useSimRcd = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
