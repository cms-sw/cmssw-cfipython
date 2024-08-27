import FWCore.ParameterSet.Config as cms

def SiPixelLorentzAngleReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelLorentzAngleReader',
    recoLabel = cms.string(''),
    simLabel = cms.string(''),
    printDebug = cms.untracked.uint32(10),
    useSimRcd = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
