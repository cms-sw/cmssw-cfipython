import FWCore.ParameterSet.Config as cms

def TestDQMGlobalEDAnalyzer(**kwargs):
  mod = cms.EDProducer('TestDQMGlobalEDAnalyzer',
    folder = cms.string('Global/testglobal'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
