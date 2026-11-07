import FWCore.ParameterSet.Config as cms

def MEtoEDMConverter(*args, **kwargs):
  mod = cms.EDProducer('MEtoEDMConverter',
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0),
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.required.untracked.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
