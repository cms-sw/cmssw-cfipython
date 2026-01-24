import FWCore.ParameterSet.Config as cms

def MPIReceiver(*args, **kwargs):
  mod = cms.EDProducer('MPIReceiver',
    upstream = cms.InputTag('source'),
    products = cms.VPSet(
      template = cms.PSetTemplate(
        type = cms.required.string,
        label = cms.string('')
      )
    ),
    instance = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
