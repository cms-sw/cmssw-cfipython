import FWCore.ParameterSet.Config as cms

def TestPortableTranscriber(*args, **kwargs):
  mod = cms.EDProducer('TestPortableTranscriber',
    source = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
