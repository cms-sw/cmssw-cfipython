import FWCore.ParameterSet.Config as cms

def EDMtoMEConverter(*args, **kwargs):
  mod = cms.EDProducer('EDMtoMEConverter',
    runInputTag = cms.required.InputTag,
    lumiInputTag = cms.required.InputTag,
    Name = cms.required.untracked.string,
    Verbosity = cms.untracked.int32(0),
    Frequency = cms.untracked.int32(50),
    convertOnEndLumi = cms.untracked.bool(True),
    convertOnEndRun = cms.untracked.bool(True),
    reScope = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
