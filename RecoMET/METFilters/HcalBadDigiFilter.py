import FWCore.ParameterSet.Config as cms

def HcalBadDigiFilter(*args, **kwargs):
  mod = cms.EDFilter('HcalBadDigiFilter',
    hbheRecHitsLabel = cms.InputTag('hbhereco'),
    unpackerReportLabel = cms.InputTag('hcalDigis'),
    debug = cms.bool(False),
    listOfFlags = cms.vstring(
      'HBHERun3BadCapId',
      'HBHERun3NonrotatingCapId',
      'HBHERun3StuckADC',
      'HBHERun3repeatedADCblock'
    ),
    minRecHitEnergies = cms.vdouble(
      -100,
      -100,
      10,
      10
    ),
    maxBadChannels = cms.uint32(5),
    useBadChannelsTopology = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
