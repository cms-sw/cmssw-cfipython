import FWCore.ParameterSet.Config as cms

def DQMScaleToClient(*args, **kwargs):
  mod = cms.EDProducer('DQMScaleToClient',
    outputme = cms.PSet(
      folder = cms.string(''),
      name = cms.string(''),
      factor = cms.double(1)
    ),
    inputme = cms.PSet(
      folder = cms.string(''),
      name = cms.string('')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
