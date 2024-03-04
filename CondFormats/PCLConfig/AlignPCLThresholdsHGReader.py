import FWCore.ParameterSet.Config as cms

def AlignPCLThresholdsHGReader(**kwargs):
  mod = cms.EDAnalyzer('AlignPCLThresholdsHGReader',
    printDebug = cms.untracked.bool(True),
    outputFile = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
