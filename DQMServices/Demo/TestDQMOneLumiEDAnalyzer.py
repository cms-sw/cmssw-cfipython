import FWCore.ParameterSet.Config as cms

def TestDQMOneLumiEDAnalyzer(**kwargs):
  mod = cms.EDProducer('TestDQMOneLumiEDAnalyzer',
    folder = cms.string('One/testonelumi'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
