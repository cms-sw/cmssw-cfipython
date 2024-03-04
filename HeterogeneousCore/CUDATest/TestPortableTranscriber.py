import FWCore.ParameterSet.Config as cms

def TestPortableTranscriber(**kwargs):
  mod = cms.EDProducer('TestPortableTranscriber',
    source = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
