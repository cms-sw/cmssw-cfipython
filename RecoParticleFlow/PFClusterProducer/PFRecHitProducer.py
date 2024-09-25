import FWCore.ParameterSet.Config as cms

def PFRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('PFRecHitProducer',
    navigator = cms.PSet(
      name = cms.string(''),
      hcalEnums = cms.vint32(),
      barrel = cms.PSet(),
      endcap = cms.PSet(),
      hgcee = cms.PSet(
        name = cms.string(''),
        topologySource = cms.string('')
      ),
      hgcheb = cms.PSet(
        name = cms.string(''),
        topologySource = cms.string('')
      ),
      hgchef = cms.PSet(
        name = cms.string(''),
        topologySource = cms.string('')
      )
    ),
    producers = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
