import FWCore.ParameterSet.Config as cms

def TestDQMOneFillRunEDAnalyzer(**kwargs):
  mod = cms.EDProducer('TestDQMOneFillRunEDAnalyzer',
    folder = cms.string('One/testonefillrun'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
