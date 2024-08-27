import FWCore.ParameterSet.Config as cms

def DQMScaleToClient(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
