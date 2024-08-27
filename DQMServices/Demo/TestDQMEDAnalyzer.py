import FWCore.ParameterSet.Config as cms

def TestDQMEDAnalyzer(**kwargs):
  mod = cms.EDProducer('TestDQMEDAnalyzer',
    folder = cms.string('Normal/test'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
