import FWCore.ParameterSet.Config as cms

def EcalEBPhase2TPParamProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalEBPhase2TPParamProducer',
    inputFile = cms.required.FileInPath,
    outputFile = cms.required.untracked.string,
    nSamplesToUse = cms.uint32(8),
    useBXPlusOne = cms.bool(False),
    phaseShift = cms.double(2.581),
    nWeightGroups = cms.uint32(61200),
    Et_sat = cms.double(1998.36),
    xtal_LSB = cms.double(0.0488),
    binOfMaximum = cms.uint32(6),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
