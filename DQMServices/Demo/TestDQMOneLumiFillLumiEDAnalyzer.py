import FWCore.ParameterSet.Config as cms

def TestDQMOneLumiFillLumiEDAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('TestDQMOneLumiFillLumiEDAnalyzer',
    folder = cms.string('One/testonelumifilllumi'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
