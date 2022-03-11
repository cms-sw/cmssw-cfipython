import FWCore.ParameterSet.Config as cms

dummyHepMCAnalyzer = cms.EDAnalyzer('DummyHepMCAnalyzer',
  dumpHepMC = cms.untracked.bool(True),
  dumpPDF = cms.untracked.bool(False),
  checkPDG = cms.untracked.bool(False),
  src = cms.InputTag('generatorSmeared'),
  mightGet = cms.optional.untracked.vstring
)
