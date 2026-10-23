import FWCore.ParameterSet.Config as cms

def DummyHepMCAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DummyHepMCAnalyzer',
    dumpHepMC = cms.untracked.bool(True),
    dumpPDF = cms.untracked.bool(False),
    checkPDG = cms.untracked.bool(False),
    src = cms.InputTag('generatorSmeared'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
