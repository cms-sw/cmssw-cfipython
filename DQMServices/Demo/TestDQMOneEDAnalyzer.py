import FWCore.ParameterSet.Config as cms

def TestDQMOneEDAnalyzer(**kwargs):
  mod = cms.EDProducer('TestDQMOneEDAnalyzer',
    folder = cms.string('One/testone'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
