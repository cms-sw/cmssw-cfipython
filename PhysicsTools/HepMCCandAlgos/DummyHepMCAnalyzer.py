import FWCore.ParameterSet.Config as cms

def DummyHepMCAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DummyHepMCAnalyzer',
    dumpHepMC = cms.untracked.bool(True),
    dumpPDF = cms.untracked.bool(False),
    checkPDG = cms.untracked.bool(False),
    src = cms.InputTag('generatorSmeared'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
