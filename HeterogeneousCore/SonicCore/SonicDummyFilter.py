import FWCore.ParameterSet.Config as cms

def SonicDummyFilter(**kwargs):
  mod = cms.EDFilter('SonicDummyFilter',
    Client = cms.PSet(
      mode = cms.string('PseudoAsync'),
      allowedTries = cms.untracked.uint32(0),
      verbose = cms.untracked.bool(False),
      factor = cms.int32(-1),
      wait = cms.int32(10),
      fails = cms.uint32(0)
    ),
    input = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
