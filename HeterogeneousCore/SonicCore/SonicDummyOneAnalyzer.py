import FWCore.ParameterSet.Config as cms

def SonicDummyOneAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SonicDummyOneAnalyzer',
    Client = cms.PSet(
      mode = cms.string('PseudoAsync'),
      allowedTries = cms.untracked.uint32(0),
      verbose = cms.untracked.bool(False),
      factor = cms.int32(-1),
      wait = cms.int32(10),
      fails = cms.uint32(0)
    ),
    input = cms.required.int32,
    expected = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
