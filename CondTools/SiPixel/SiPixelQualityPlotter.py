import FWCore.ParameterSet.Config as cms

def SiPixelQualityPlotter(**kwargs):
  mod = cms.EDAnalyzer('SiPixelQualityPlotter',
    useLogScale = cms.bool(False),
    addLumiInfo = cms.bool(True),
    analyzedTag = cms.string(''),
    maxRun = cms.untracked.uint32(999999),
    lumiInputTag = cms.untracked.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
