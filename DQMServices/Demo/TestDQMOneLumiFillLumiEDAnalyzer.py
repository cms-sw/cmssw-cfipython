import FWCore.ParameterSet.Config as cms

def TestDQMOneLumiFillLumiEDAnalyzer(**kwargs):
  mod = cms.EDProducer('TestDQMOneLumiFillLumiEDAnalyzer',
    folder = cms.string('One/testonelumifilllumi'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
