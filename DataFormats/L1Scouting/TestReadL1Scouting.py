import FWCore.ParameterSet.Config as cms

def TestReadL1Scouting(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadL1Scouting',
    bxValues = cms.required.vuint32,
    expectedMuonValues = cms.required.vint32,
    muonsTag = cms.required.InputTag,
    expectedJetValues = cms.required.vint32,
    jetsTag = cms.required.InputTag,
    expectedEGammaValues = cms.required.vint32,
    eGammasTag = cms.required.InputTag,
    expectedTauValues = cms.required.vint32,
    tausTag = cms.required.InputTag,
    expectedBxSumsValues = cms.required.vint32,
    bxSumsTag = cms.required.InputTag,
    bmtfStubClassVersion = cms.required.int32,
    expectedBmtfStubValues = cms.required.vint32,
    bmtfStubTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
